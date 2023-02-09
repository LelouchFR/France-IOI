program Solution;
var
    legumes, i: LongInt;
    weight, age, price: Double;
begin
    read(legumes);
    for i := 1 to legumes do
    begin
        read(weight, age, price);
        writeln(price / weight);
    end;
end.