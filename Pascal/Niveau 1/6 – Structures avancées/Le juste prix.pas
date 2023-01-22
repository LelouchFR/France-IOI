program Solution;
var
    sellers, minPrice, posMinPrice, pos, i, price: LongInt;
begin
    read(sellers);
    minPrice := 1000 * 1000;
    posMinPrice := -1;
    pos := 1;
    for i := 1 to sellers do
    begin
        read(price);
        if price <= minPrice then
        begin
            minPrice := price;
            posMinPrice := pos;
        end;
        pos := pos + 1;
    end;
    writeln(posMinPrice);
end.