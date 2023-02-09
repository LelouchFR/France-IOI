program Solution;
var
    lines, i, j, variation: LongInt;
    quantity: array[1..10] of LongInt = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
begin
    read(lines);
    for i := 1 to lines do
    begin
        read(j, variation);
        quantity[j] := quantity[j] + variation;
    end;
    for i := 1 to 10 do
    begin
        writeln(quantity[i]);
    end;
end.