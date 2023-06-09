CREATE PROCEDURE SP_INSERIR_NOTICIA
    @LINK NVARCHAR(4000)
AS
BEGIN

    DECLARE @NUM_REGISTRO_EXISTENTES INT = (
        SELECT COUNT(1)
        FROM NOTICIA (NOLOCK)
        WHERE LINK = @LINK
    )

    IF @NUM_REGISTRO_EXISTENTES < 1
    BEGIN
        INSERT INTO NOTICIA (LINK) VALUES
            (@LINK)
    END

END