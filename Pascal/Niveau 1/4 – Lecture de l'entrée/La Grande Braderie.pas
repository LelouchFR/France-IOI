program Solution;
var
   startpos, larg, sellers, i: LongInt;
begin
   read(startpos);
   read(larg);
   read(sellers);
   
   writeln(startpos);
   
   for i := 1 to sellers do
   begin
      startpos := startpos + larg;
      writeln(startpos);
   end;
end.