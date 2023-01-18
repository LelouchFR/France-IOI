program Solution;
var
   cubes, larg, i: LongInt;
begin
   cubes := 0;
   larg := 1;
   for i := 1 to 9 do
   begin
      cubes := cubes + larg * larg * larg;
      larg := larg + 2;
   end;
   write(cubes);
end.