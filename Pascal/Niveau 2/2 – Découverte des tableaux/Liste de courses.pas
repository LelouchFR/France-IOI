program Solution;
var
    tot, choice, i: LongInt;
    ingr: array[0..9] of LongInt = (9, 5, 12, 15, 7, 42, 13, 10, 1, 20);
begin
    tot := 0;
    for i := 0 to 9 do
    begin
        read(choice);
        tot := tot + choice * ingr[i];
    end;
    writeln(tot);
end.