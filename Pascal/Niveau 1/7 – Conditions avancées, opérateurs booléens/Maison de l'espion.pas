program Solution;
var
   xMin, xMax, yMin, yMax, houses, dig, x, y, i: LongInt;
begin
   read(xMin, xMax, yMin, yMax, houses);
   dig := 0;
   for i := 1 to houses do
   begin
      read(x, y);
      if (xMin <= x) and (x <= xMax) and (yMin <= y) and (y <= yMax) then
      begin
         dig := dig + 1;
      end;
   end;
   writeln(dig);
end.