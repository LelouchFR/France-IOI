program Solution;
var
    mesures, tempMin, tempMax, mesure, temp: LongInt;
    validTemp: Boolean;
begin
    read(mesures, tempMin, tempMax);
    mesure := 0;
    validTemp := true;
    while (mesure < mesures) and (validTemp) do
    begin
        read(temp);
        validTemp := (tempMin <= temp) and (temp <= tempMax);
        if validTemp then
        begin
            writeln('Rien à signaler');
        end
        else
        begin
            writeln('Alerte !!');
        end;
    mesure := mesure + 1;
    end;
end.