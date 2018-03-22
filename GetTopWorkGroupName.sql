IF OBJECT_ID('dbo.GetTopWorkGroupName') IS NOT NULL
DROP FUNCTION GetTopWorkGroupName
GO

CREATE FUNCTION GetTopWorkGroupName
(@WorkGroupId NVARCHAR(50))
RETURNS NVARCHAR(50)
AS
BEGIN
	DECLARE @PWorkGroupId NVARCHAR(50)
	SET @PWorkGroupId = (SELECT PWorkGroupId FROM dbo.WorkGroup wg WHERE wg.WorkGroupId = @WorkGroupId)

	WHILE ((SELECT WorkGroupName FROM dbo.WorkGroup wg WHERE wg.WorkGroupId = @PWorkGroupId) IS NOT NULL)
	BEGIN
		SELECT @WorkGroupId = @PWorkGroupId
		SELECT @PWorkGroupId = (SELECT PWorkGroupId FROM dbo.WorkGroup wg WHERE wg.WorkGroupId = @PWorkGroupId)
	END

	RETURN (SELECT WorkGroupName FROM dbo.WorkGroup wg WHERE wg.WorkGroupId = @WorkGroupId)
END