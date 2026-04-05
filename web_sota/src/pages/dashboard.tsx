import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Activity, Layers, Zap, Music, Play, Square } from "lucide-react";
import { Badge } from "@/components/ui/badge";

const BLEND_MODES = ["Normal","Add","Subtract","Multiply","Screen","Overlay","Hard Light","Soft Light","Color Dodge","Color Burn","Darken","Lighten"];

export function Dashboard() {
    return (
        <div className="space-y-6">
            <div className="flex items-center justify-between">
                <div>
                    <h2 className="text-2xl font-bold tracking-tight text-white">Resolume Arena</h2>
                    <p className="text-slate-400">VJ performance control — OSC bridge on ports 7000/7001</p>
                </div>
                <Badge variant="outline" className="border-emerald-500 text-emerald-400">OSC Active</Badge>
            </div>

            {/* KPI Cards */}
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
                <Card className="border-slate-800 bg-slate-950/50">
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium text-slate-200">OSC Bridge</CardTitle>
                        <Activity className="h-4 w-4 text-emerald-500" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold text-white">7000/7001</div>
                        <p className="text-xs text-slate-400">In/Out UDP ports</p>
                    </CardContent>
                </Card>

                <Card className="border-slate-800 bg-slate-950/50">
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium text-slate-200">Layers</CardTitle>
                        <Layers className="h-4 w-4 text-blue-500" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold text-white">1–8</div>
                        <p className="text-xs text-slate-400">opacity · bypass · blend</p>
                    </CardContent>
                </Card>

                <Card className="border-slate-800 bg-slate-950/50">
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium text-slate-200">Clips/Layer</CardTitle>
                        <Play className="h-4 w-4 text-purple-500" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold text-white">1–10</div>
                        <p className="text-xs text-slate-400">load · trigger · position</p>
                    </CardContent>
                </Card>

                <Card className="border-slate-800 bg-slate-950/50">
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium text-slate-200">BPM Sync</CardTitle>
                        <Music className="h-4 w-4 text-orange-500" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold text-white">60–200</div>
                        <p className="text-xs text-slate-400">tempo-synced effects</p>
                    </CardContent>
                </Card>
            </div>

            {/* Tool Reference */}
            <div className="grid gap-4 md:grid-cols-2">
                <Card className="border-slate-800 bg-slate-950/50">
                    <CardHeader>
                        <CardTitle className="text-white flex items-center gap-2">
                            <Zap className="h-4 w-4 text-yellow-400" /> MCP Tools
                        </CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-2 text-sm">
                        <div className="flex justify-between border-b border-slate-800 pb-1">
                            <span className="font-mono text-purple-300">clip_control</span>
                            <span className="text-slate-400">load · trigger · clear · position · opacity</span>
                        </div>
                        <div className="flex justify-between border-b border-slate-800 pb-1">
                            <span className="font-mono text-purple-300">layer_control</span>
                            <span className="text-slate-400">opacity · bypass · blend_mode · transition</span>
                        </div>
                        <div className="flex justify-between border-b border-slate-800 pb-1">
                            <span className="font-mono text-purple-300">effect_control</span>
                            <span className="text-slate-400">parameter · bypass</span>
                        </div>
                        <div className="flex justify-between">
                            <span className="font-mono text-purple-300">performance_control</span>
                            <span className="text-slate-400">bpm · batch_update</span>
                        </div>
                    </CardContent>
                </Card>

                <Card className="border-slate-800 bg-slate-950/50">
                    <CardHeader>
                        <CardTitle className="text-white flex items-center gap-2">
                            <Layers className="h-4 w-4 text-blue-400" /> Blend Modes
                        </CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="grid grid-cols-3 gap-1">
                            {BLEND_MODES.map((name, i) => (
                                <div key={i} className="flex items-center gap-1 text-xs">
                                    <span className="text-slate-500 font-mono w-4">{i}</span>
                                    <span className="text-slate-300">{name}</span>
                                </div>
                            ))}
                        </div>
                    </CardContent>
                </Card>
            </div>

            {/* OSC Quick Reference */}
            <Card className="border-slate-800 bg-slate-950/50">
                <CardHeader>
                    <CardTitle className="text-white flex items-center gap-2">
                        <Square className="h-4 w-4 text-slate-400" /> OSC Address Quick Reference
                    </CardTitle>
                </CardHeader>
                <CardContent>
                    <div className="font-mono text-xs space-y-1 text-slate-400">
                        <p><span className="text-blue-300">/composition/layers/{"{L}"}/clips/{"{C}"}/connect</span> — trigger clip</p>
                        <p><span className="text-blue-300">/composition/layers/{"{L}"}/clips/{"{C}"}/transport/position</span> — scrub 0.0–1.0</p>
                        <p><span className="text-blue-300">/composition/layers/{"{L}"}/clips/{"{C}"}/video/opacity</span> — clip opacity</p>
                        <p><span className="text-blue-300">/composition/layers/{"{L}"}/opacity</span> — layer opacity</p>
                        <p><span className="text-blue-300">/composition/layers/{"{L}"}/bypassed</span> — layer on/off</p>
                        <p><span className="text-blue-300">/composition/layers/{"{L}"}/blending/mode</span> — blend mode 0–11</p>
                        <p><span className="text-blue-300">/composition/layers/{"{L}"}/effects/{"{E}"}/params/{"{P}"}/value</span> — effect param</p>
                        <p><span className="text-blue-300">/composition/tempomap/bpm</span> — master BPM</p>
                    </div>
                </CardContent>
            </Card>
        </div>
    );
}
