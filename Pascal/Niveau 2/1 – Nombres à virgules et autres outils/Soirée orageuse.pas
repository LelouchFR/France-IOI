program Solution;
var
    vSon, tParcours: Double;
    dist: LongInt;
begin
    vSon := 340.29;
    read(tParcours);
    dist := round((tParcours * vSon) / 1000);
    writeln(dist);
end.