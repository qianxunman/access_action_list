--end stock_quant_group
--==============================================================
-- 进销存
drop view if exists view_in_out_inventory;

drop function if exists func_in_out_inventory cascade;
create or replace function func_in_out_inventory()
    returns table
            (
                product_id       int,
                location_dest_id int,
                lot_id           int,
--                 month            varchar,
                date_month       date,
                product_uom_id   int,
                qty_done         float,
                type             varchar
            )
as
$$
declare
    var_month date;
begin
    drop table if exists tb_move_line_month;
    create temporary table tb_move_line_month as
    select *,
           "left"(write_date :: varchar, 7)                  as month,
           ("left"(write_date :: varchar, 7) || '-01')::date as date_month,
           write_date::date                                  as date_write_date
    from stock_move_line
    where state = 'done';

-- 查看某个位置的出库信息:
    drop table if exists tb_location_out;
    create temporary table tb_location_out as
    select A.product_id,
           A.location_id,
           A.lot_id,
           A.month,
           A.date_month,
           A.date_write_date,
           A.product_uom_id,
           -sum(A.qty_done) as qty_done,
           '2outgoing'      as type
    from tb_move_line_month as A
    group by A.product_id, A.location_id, A.lot_id, A.month, A.date_month, A.date_write_date, A.product_uom_id;

-- 查看某个位置的入库信息:
    drop table if exists tb_location_in;
    create temporary table tb_location_in as
    select A.product_id,
           A.location_dest_id,
           A.lot_id,
           A.month,
           A.date_month,
           A.date_write_date,
           A.product_uom_id,
           sum(A.qty_done) as qty_done,
           '1incoming'     as type
    from tb_move_line_month as A
    group by A.product_id, A.location_dest_id, A.lot_id, A.month, A.date_month, A.date_write_date, A.product_uom_id;

    drop table if exists tb_location_union;
    create temporary table tb_location_union as
    select *
    from tb_location_in
    union
    select *
    from tb_location_out;

--     获取每个月的结存
    drop table if exists tb_add_inventory;
    create temporary table tb_add_inventory
    (
        product_id       int,
        location_dest_id int,
        lot_id           int,
--         month            varchar,
        date_month       date,
        product_uom_id   int,
        qty_done         float,
        type             varchar

    );

    for var_month in select distinct A.date_month
                     from tb_location_union as A
        loop
            insert into tb_add_inventory
            select A.product_id,
                   A.location_dest_id,
                   A.lot_id,
                   var_month       as date_month,
                   A.product_uom_id,
                   sum(A.qty_done) as qty_done,
                   '3inventory'    as type
            from tb_location_union as A
            where A.date_month <= var_month
            group by A.product_id, A.location_dest_id, A.lot_id, A.product_uom_id;
        end loop;

    --     h获取每月进出:
    insert into tb_add_inventory
    select A.product_id,
           A.location_dest_id,
           A.lot_id,
           A.date_month,
           A.product_uom_id,
           sum(A.qty_done) as qty_done,
           A.type
    from tb_location_union as A
    group by A.product_id, A.location_dest_id, A.lot_id, A.date_month, A.product_uom_id, A.type;

--     出现交易比结存少的情况,正常,有结存不一定有交易.

    return query select * from tb_add_inventory;


end;
$$
    language plpgsql
    volatile;


create or replace view view_in_out_inventory as
select row_number() over (order by product_id) as id,
       product_id,
       location_dest_id                        as location_id,
       lot_id,
       date_month,
       "left"(date_month::varchar, 7)          as format_month,
       product_uom_id,
       qty_done,
       type
from func_in_out_inventory();


-- 按日期查找单据并将所有数据汇总.
-- select *
-- from stock_move_line;
-- select *
-- from view_in_out_inventory;


-- 存在缺陷:
/*
1. odoo 可以实现日期格式的自动选择,我这里直接弄一个月份的格式,固定得太死了,应该要按照天来汇总才合理
 需要更改为按天统计得进销存.

2. 性能上的优化,


 */


