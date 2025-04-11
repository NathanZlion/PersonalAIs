
export default function ChatLayout({
    children,
}: Readonly<{ children: React.ReactNode }>) {
    return (
        <div className="flex flex-1 flex-col gap-4 md:m-5 rounded-lg outline-[0.3px] bg-slate-100 dark:bg-muted overflow-auto">
            {children}
        </div>
    );
}