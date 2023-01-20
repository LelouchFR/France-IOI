program Solution;
var
   firstDeg, secondDeg, sum: integer;
begin
   read(firstDeg, secondDeg);
   sum := firstDeg + secondDeg;
   if sum >= 10 then
   begin
      writeln('Taxe spéciale !');
      writeln(36);
   end
   else
   begin
      writeln('Taxe régulière');
      writeln(2 * sum);
   end;
end.