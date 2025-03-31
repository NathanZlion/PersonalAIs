import { Avatar, AvatarFallback, AvatarImage } from "./ui/avatar";


export default function LogoComponent(
) {
    return (
        <Avatar>
            <AvatarImage src="/logo.jpg" alt="A" />
            <AvatarFallback>P</AvatarFallback>
        </Avatar>
    );
}