program Solution;
var
    height, folioles: LongInt;
    list: array[1..4] of string;
begin
    list[1] := 'Tinuviel';
    list[2] := 'Falarion';
    list[3] := 'Dorthonion';
    list[4] := 'Calaelen';
    read(height, folioles);
    if height < 9 then
    begin
        if folioles > 6 then
        begin
            writeln(list[1]);
        end
        else
        begin
            writeln(list[2]);
        end;
    end
    else
    begin
        if folioles < 8 then
        begin
            writeln(list[3]);
        end
        else
        begin
            writeln(list[4]);
        end;
    end;
end.
