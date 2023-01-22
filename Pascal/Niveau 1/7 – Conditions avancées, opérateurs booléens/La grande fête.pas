program Solution;
var
   starts, ends, i, spyS, spyE, invites, sus: LongInt;
begin
   read(spyS, spyE, invites);
   sus := 0;
   for i := 1 to invites do
   begin
      read(starts, ends);
      if not((spyE < starts) or (ends < spyS)) then
      begin
         sus := sus + 1;
      end;
   end;
   writeln(sus);
end.