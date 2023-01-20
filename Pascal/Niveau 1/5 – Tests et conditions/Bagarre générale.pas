program Solution;
var
   champE, champA: LongInt;
begin
   read(champE, champA);
   if champA > champE then
   begin
      if champA - champE > 10 then
      begin
         writeln('La famille Evaran a un champ trop grand');
      end
      else
      begin
         writeln;
      end;
   end
   else if champE > champA then
   begin
      if champE - champA > 10 then
      begin
         writeln('La famille Arignon a un champ trop grand');
      end;
   end;
end.