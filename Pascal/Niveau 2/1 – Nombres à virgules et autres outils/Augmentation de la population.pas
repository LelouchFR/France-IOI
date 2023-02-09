program Solution;
var
    pop: LongInt;
    croissance: Double;
begin
    read(pop, croissance);
    pop := trunc(pop * (1 + croissance / 100));
    writeln(pop);
end.