program Solution;
var
   i: LongInt;
   craps: LongInt;
begin
   craps := 1337;
   for i := 1 to 12 do
   begin
      craps := craps * 2;
   end;
   write(craps);
end.