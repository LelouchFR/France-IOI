program Solution;
uses Robot;
var
   i: LongInt;
begin
   for i := 1 to 2 do gauche;
   writeln('Bonjour, laissez-moi vous aider');
   ramasser;
   for i := 1 to 32 do
   begin
      droite;
   end;
   deposer;
end.