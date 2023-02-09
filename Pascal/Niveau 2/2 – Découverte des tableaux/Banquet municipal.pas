program Solution;
var
    ids: array of LongInt;
    persons, person, changes, change, first, second, temp: LongInt;
begin
    read(persons, changes);
    setLength(ids, persons);
    for person := 0 to (persons - 1) do
    begin
        read(ids[person]);
    end;
    for change := 1 to changes do
    begin
        read(first, second);
        temp := ids[first];
        ids[first] := ids[second];
        ids[second] := temp;
    end;
    for person := 0 to (persons - 1) do
    begin
        writeln(ids[person]);
    end;
end.