import { API_BASE } from "../lib/api";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ExternalLink } from "lucide-react";

export function ApiDocsPage() {
  const backendUrl = API_BASE;
  return (
    <div className="space-y-6" data-testid="api-docs-page">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-white">API Documentation</h1>
          <p className="text-sm text-slate-400 mt-1">FastAPI auto-generated docs for the Resolume MCP REST API</p>
        </div>
        <a href={`${backendUrl}/docs`} target="_blank" rel="noopener noreferrer"
           className="flex items-center gap-2 text-sm text-blue-400 hover:text-blue-300">
          <ExternalLink className="h-4 w-4" /> Open in browser
        </a>
      </div>
      <div className="grid gap-4 md:grid-cols-3">
        <Card className="border-slate-800 bg-slate-950/50">
          <CardHeader><CardTitle className="text-sm text-slate-200">Health</CardTitle></CardHeader>
          <CardContent className="text-xs text-slate-400 space-y-1">
            <code className="block text-emerald-400">GET /health</code>
          </CardContent>
        </Card>
        <Card className="border-slate-800 bg-slate-950/50">
          <CardHeader><CardTitle className="text-sm text-slate-200">Tools</CardTitle></CardHeader>
          <CardContent className="text-xs text-slate-400 space-y-1">
            <code className="block text-blue-400">help, status</code>
            <code className="block text-amber-400">clip_control, layer_control</code>
            <code className="block text-amber-400">effect_control, performance_control</code>
          </CardContent>
        </Card>
        <Card className="border-slate-800 bg-slate-950/50">
          <CardHeader><CardTitle className="text-sm text-slate-200">OSC</CardTitle></CardHeader>
          <CardContent className="text-xs text-slate-400 space-y-1">
            <code className="block text-purple-400">OSC UDP on ports 7000/7001</code>
            <code className="block text-purple-400">MCP HTTP at port 11140</code>
          </CardContent>
        </Card>
      </div>
      <iframe src={`${backendUrl}/docs`} className="w-full border-0 rounded-lg" style={{ height: "70vh", filter: "invert(0.9) hue-rotate(180deg)" }}
              title="Swagger UI" />
    </div>
  );
}
