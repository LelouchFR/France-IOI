program Solution;
var
    tot, i, notes, note: LongInt;
begin
    read(notes);
    tot := 0;
    for i := 1 to notes do
    begin
        read(note);
        tot := tot + note;
    end;
    writeln(tot / notes);
end.