program Solution;
var
   i, jetons, x, y: LongInt;
begin
   read(jetons);
   for i := 1 to jetons do
   begin
      read(x, y);
      if (x < 0) or (x > 90) or (y < 0) or (y > 70) then
      begin
         writeln('En dehors de la feuille');
      end
      else if (y > 60) and (((x > 15) and (x < 45)) or ((x > 60) and (x < 85))) then
      begin
         writeln('Dans une zone rouge');
      end
      else if (x > 10) and (x < 85) and (y > 10) and (y < 55) and not((x > 25) and (x < 50) and (y > 20) and (y < 45)) then
      begin
         writeln('Dans une zone bleue');
      end
      else
      begin
         writeln('Dans une zone jaune');
      end;
   end;
end.