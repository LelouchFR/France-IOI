program Solution;
var
   i, posA, villages, access, gap, posV: LongInt;
begin
   read(posA, villages);
   access := 0;
   for i := 1 to villages do
   begin
      read(posV);
      gap := posA - posV;
      if gap < 0 then
      begin
         gap := -gap;
      end;
      if gap <= 50 then
      begin
         access := access + 1;
      end;
   end;
   writeln(access);
end.