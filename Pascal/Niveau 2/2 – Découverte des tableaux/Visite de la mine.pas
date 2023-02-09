program Solution;
var
    invertDep: array[1..5] of LongInt = (2, 1, 3, 5, 4);
    way: array of LongInt;
    deplacements, i, deplacement: LongInt;
begin
    read(deplacements);
    setLength(way, deplacements);
    for i := 0 to (deplacements - 1) do
    begin
        read(way[i]);
    end;
    for i := (deplacements - 1) downto 0 do
    begin
        deplacement := way[i];
        writeln(invertDep[deplacement]);
    end;
end.