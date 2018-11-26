using System;
using System.Collections.Generic;

namespace VideoFrameAnalyzer
{
    public static class People
    {
        public static Dictionary<Guid, string> Names = new Dictionary<Guid, string>
        {
            { new Guid("dc2a4c0c-797c-4939-8930-5aa9b0353bff"), "Kosta" },
            { new Guid("50003e53-089d-4e4b-8945-4c0f4fab83c6"), "Jasmina" }
        };
    }
}
