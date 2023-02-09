program Solution;
var
    ingr: LongInt;
    quantity: array[0..9] of LongInt = (500, 180, 650, 25, 666, 42, 421, 1, 370, 211);
begin
    read(ingr);
    writeln(quantity[ingr]);
end.