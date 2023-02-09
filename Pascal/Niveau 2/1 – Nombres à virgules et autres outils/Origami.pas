program Solution;
var
    eppaisseur: Double;
    i: LongInt;
begin
    eppaisseur := 0.11;
    for i := 1 to 15 do
    begin
        eppaisseur := eppaisseur * 2;
    end;
    writeln(eppaisseur / 10);
end.