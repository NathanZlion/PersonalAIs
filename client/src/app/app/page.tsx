

export default function Page({
    children,
}: Readonly<{ children: React.ReactNode }>) {
    return (
        <div className="flex flex-col items-center justify-center w-full h-full">
            <h1 className="text-4xl font-bold">Welcome to PersonalAIs</h1>
            <p className="mt-4 text-lg">Your advanced AI agent for music.</p>
        </div>
    );
}