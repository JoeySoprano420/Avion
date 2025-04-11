Imports System
Imports System.Collections.Generic
Imports System.IO
Imports System.Text

Module AvionCompiler

    Sub Main(args As String())
        Console.WriteLine("✦ Avion Compiler Engine Initializing...")

        If args.Length = 0 Then
            Console.WriteLine("Usage: AvionCompiler <solutionPath> [--run] [--debug]")
            Return
        End If

        Dim solutionPath As String = args(0)
        Dim runAfterCompile As Boolean = args.Contains("--run")
        Dim debugMode As Boolean = args.Contains("--debug")

        Console.WriteLine("⇲ Loading Avion solution from path: " & solutionPath)

        Dim projects = LoadProjects(solutionPath)
        If projects.Count = 0 Then
            Console.WriteLine("✖ No Avion projects found in path.")
            Return
        End If

        For Each proj In projects
            Try
                Console.WriteLine("⟳ Parsing: " & proj.EntryPath)
                Dim sourceCode As String = File.ReadAllText(proj.EntryPath)
                Dim ast = ParseToAST(sourceCode)

                Console.WriteLine("⟳ Compiling to Bytecode...")
                Dim bytecode As Byte() = CompileToBytecode(ast)
                Dim outputPath = Path.Combine("bin", proj.Name & ".avb")

                Directory.CreateDirectory("bin")
                File.WriteAllBytes(outputPath, bytecode)

                Console.WriteLine("✔ Compiled '" & proj.Name & "' to '" & outputPath & "'")

                If runAfterCompile Then
                    Console.WriteLine("▶ Running bytecode with AvionVM...")
                    ExecuteBytecode(bytecode, debugMode)
                End If

            Catch ex As Exception
                Console.WriteLine("✖ Compilation failed for project: " & proj.Name)
                Console.WriteLine("↳ " & ex.Message)
                RenderGlyphError(ex.Message)
            End Try
        Next

        Console.WriteLine("✓ All compilations finished.")
    End Sub

    Function LoadProjects(path As String) As List(Of AvionProject)
        Dim list As New List(Of AvionProject)()
        For Each file In Directory.GetFiles(path, "*.avproj", SearchOption.AllDirectories)
            list.Add(New AvionProject With {
                .Name = Path.GetFileNameWithoutExtension(file),
                .EntryPath = file.Replace(".avproj", ".av")
            })
        Next
        Return list
    End Function

    Function ParseToAST(source As String) As String
        ' Simulate AST for demo purpose
        Return "AST(" & source.Substring(0, Math.Min(20, source.Length)) & "...)"
    End Function

    Function CompileToBytecode(ast As String) As Byte()
        ' Simulate bytecode output (placeholder)
        Return Encoding.UTF8.GetBytes("BYTECODE<" & ast & ">")
    End Function

    Sub ExecuteBytecode(bytes As Byte(), debug As Boolean)
        Console.WriteLine("〄 [AvionVM] Executing...")
        If debug Then Console.WriteLine("➤ Stack initialized at 0x0001")
        Console.WriteLine("⋄ Bytecode length: " & bytes.Length & " bytes")
        Console.WriteLine("⋄ Output:\n" & Encoding.UTF8.GetString(bytes))
    End Sub

    Sub RenderGlyphError(message As String)
        Console.WriteLine("☠ Avion Glyph Error:")
        Console.WriteLine("  ⚑⚐⚑ :: " & message & " :: ⚑⚐⚑")
    End Sub

    Class AvionProject
        Public Property Name As String
        Public Property EntryPath As String
    End Class

End Module
