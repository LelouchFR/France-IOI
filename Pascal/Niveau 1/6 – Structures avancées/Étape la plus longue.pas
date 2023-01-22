program Solution;
var
   i, days, distMax, dist: LongInt;
begin
   read(days);
   distMax := 0;
   for i := 1 to days do
   begin
      read(dist);
      if dist > distMax then
      begin
         distMax := dist;
      end;
   end;
   writeln(distMax);
end.