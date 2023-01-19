program Solution;
var
   i, h, input: LongInt;
begin
   read(input);
   h := 66;
   for i := 1 to input do
   begin
      h := h * i;
      writeln(h);
   end;
end.