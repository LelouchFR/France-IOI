program Solution;
var
   i: LongInt;
   j: LongInt;
begin
   for i := 1 to 20 do
   begin
      for j := 1 to 20 do
      begin
         write('OX');
      end;
      writeln;
      for j := 1 to 20 do
      begin
         write('XO');
      end;
      writeln;
   end;
end.