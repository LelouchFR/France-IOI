program Solution;
var
    toFind, proposition, tries: LongInt;
begin
    read(toFind, proposition);
    tries := 1;
    while proposition <> toFind do
    begin
        if proposition > toFind then
        begin
            writeln('c''est moins');
        end
        else
        begin
            writeln('c''est plus');
        end;
        read(proposition);
        tries := tries + 1;
    end;
    writeln('Nombre d''essais nécessaires : ');
    writeln(tries)
end.