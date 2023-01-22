program Solution;
var
   i, IDP, listSize, num: LongInt;
   hasLeft: boolean;
begin
   hasLeft := false;
   read(IDP, listSize);
   for i := 1 to listSize do
   begin
      read(num);
      if num = IDP then
      begin
         hasLeft := true;
      end;
   end;
   if hasLeft = true then
   begin
      writeln('Sorti de la ville');
   end
   else
   begin
      writeln('Encore dans la ville');
   end;
end.