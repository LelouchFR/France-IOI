program Solution;
var
    sellers: array of LongInt;
    placements, i, j: LongInt;
begin
    read(placements);
    setLength(sellers, placements);
    for i := 0 to placements - 1 do
    begin
        read(j);
        sellers[j] := i;
    end;
    for i := 0 to placements - 1 do
    begin
        writeln(sellers[i]);
    end;
end.