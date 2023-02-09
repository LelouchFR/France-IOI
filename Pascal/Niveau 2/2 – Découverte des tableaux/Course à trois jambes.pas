program Solution;
var
    nums: array of LongInt;
    persons, person, first, second: LongInt;

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
    setLength(nums, persons);
    for person := 0 to (persons - 1) do
    begin
        read(nums[person]);
    end;
    tri(nums);
    for first := 0 to (persons div 2) - 1 do
    begin
        second := persons - 1 - first;
        writeln(nums[first], ' ', nums[second]);
    end;
end.