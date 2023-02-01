program Solution;
var
    maxRocks, rocks, height: LongInt;
begin
    read(maxRocks);
    rocks := 0;
    height := 1;
    while rocks + height * height <= maxRocks do
    begin
        rocks := rocks + height * height;
        height := height + 1;
    end;
    writeln(height - 1);
    writeln(rocks);
end.