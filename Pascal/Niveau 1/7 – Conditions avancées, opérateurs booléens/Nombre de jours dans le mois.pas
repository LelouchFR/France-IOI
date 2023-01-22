program Solution;
var
   num: integer;
begin
   read(num);
   if num = 11 then
   begin
      writeln(29);
   end
   else
   begin
      if ((4 <= num)  and (num <= 6)) or (num = 10) then
      begin
         writeln(31);
      end
      else
      begin
         writeln(30);
      end;
   end;
end.