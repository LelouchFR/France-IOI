program Solution;
var
    persons, fruits: LongInt;
begin
    read(persons, fruits);
    if fruits mod persons = 0 then
    begin
       writeln('oui');
    end
    else
    begin
        writeln('non');
    end;
end.