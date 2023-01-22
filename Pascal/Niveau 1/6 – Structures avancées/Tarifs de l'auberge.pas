program Solution;
var
    age, weight: LongInt;
begin
    read(age, weight);
    if age < 10 then
    begin
       writeln(5);
    end
    else
    begin
        if age = 60 then
        begin
            writeln(0);
        end
        else
        begin
            if weight >= 20 then
            begin
               writeln(40);
            end
            else
            begin
                writeln(30);
            end;
        end;
    end;
end.