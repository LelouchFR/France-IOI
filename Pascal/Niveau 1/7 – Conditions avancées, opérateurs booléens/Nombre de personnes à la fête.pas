program Solution;
var
   persons, Max, actual, i, num: LongInt;
begin
   read(persons);
   Max := 0;
   actual := 0;
   for i := 1 to persons * 2 do
   begin
      read(num);
      if num > 0 then
      begin
         actual := actual + 1;
      end
      else
      begin
         actual := actual - 1;
      end;
      if actual > Max then
      begin
         Max := actual;
      end;
   end;
   writeln(Max);
end.