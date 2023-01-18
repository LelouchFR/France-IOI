program Solution;
var
    i: LongInt;
    j: LongInt;
begin
    for i := 1 to 3 do
    begin
        for j := 1 to 30 do
        begin
            if i = 1 then
            begin
                write('a_');
            end
            else if i = 2 then
            begin
                write('b_');
            end
            else
            begin
                write('c_');
            end;
        end;
        writeln;
    end;
end.