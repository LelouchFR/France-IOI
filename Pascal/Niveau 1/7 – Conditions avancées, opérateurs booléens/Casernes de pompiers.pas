program Solution;
var
   xMin1, xMin2, xMax1, xMax2, yMin1, yMin2, yMax1, yMax2, paires, i: LongInt;
begin
   read(paires);
   for i := 1 to paires do
   begin
      read(xMin1, xMax1, yMin1, yMax1, xMin2, xMax2, yMin2, yMax2);
      if ((xMax2 <= xMin1) or (xMax1 <= xMin2)) or ((yMax2 <= yMin1) or (yMax1 <= yMin2)) then
      begin
         writeln('NON');
      end
      else
      begin
         writeln('OUI');
      end;
   end;
end.