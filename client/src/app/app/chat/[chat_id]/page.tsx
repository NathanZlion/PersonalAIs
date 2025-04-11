
export default async function ChatPage({
    params,
}: {
    params: Promise<{ chat_id: string }>;
}) {
    const { chat_id } = await params;
    return (
        <div>
            <h1>Chat {chat_id} </h1>
            <p>Chat content goes here...</p>
        </div>
    );
}