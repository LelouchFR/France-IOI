program Solution;
var
    bags, price: LongInt;
    cimentQuantity: Double;
begin
    read(cimentQuantity);
    bags := trunc(cimentQuantity / 60);
    if bags < cimentQuantity / 60
        then bags := bags + 1;
    price := bags * 45;
    writeln(price);
end.