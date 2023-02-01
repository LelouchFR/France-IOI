program Solution;
var
    sumDepenses, depenses: LongInt;
begin
    sumDepenses := 0;
    read(depenses);
    while depenses <> -1 do
    begin
        sumDepenses := sumDepenses + depenses;
        read(depenses);
    end;
    write(sumDepenses);
end.