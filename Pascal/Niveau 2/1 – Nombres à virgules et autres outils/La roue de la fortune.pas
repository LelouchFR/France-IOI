program Solution;
var
    zones: LongInt;
begin
    read(zones);
    writeln(((zones mod 24) + 24) mod 24);
end.