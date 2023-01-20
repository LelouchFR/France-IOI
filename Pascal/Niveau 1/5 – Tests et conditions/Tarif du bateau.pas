program Solution;
var
   age: LongInt;
begin
   read(age);
   if age < 21 then
   begin
      writeln('Tarif réduit');
   end
   else
   begin
      writeln('Tarif plein');
   end;
end.