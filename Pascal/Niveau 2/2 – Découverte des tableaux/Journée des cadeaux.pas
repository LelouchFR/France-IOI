program Solution;
var
    fortune: array of LongInt;
    persons, person, mid: LongInt;

procedure tri(var vals: array of LongInt);
var
    posTwo, pos, val: LongInt;
begin
    for pos := (low(vals) + 1) to high(vals) do
    begin
        val := vals[pos];
        posTwo := pos;
        while (posTwo > low(vals)) and (val < vals[posTwo - 1]) do
        begin
            vals[posTwo] := vals[posTwo - 1];
            posTwo := posTwo - 1;
        end;
        vals[posTwo] := val;
    end;
end;

begin
    read(persons);
    setLength(fortune, persons);
    for person := 0 to (persons - 1) do
    begin
        read(fortune[person]);
    end;
    tri(fortune);
    if odd(persons) then
    begin
        mid := (persons - 1) div 2;
        writeln(fortune[mid]);
    end
    else
    begin
        mid := persons div 2;
        writeln((fortune[mid - 1] + fortune[mid]) / 2.0 :0:1)
    end;
end.